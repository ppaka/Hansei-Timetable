const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

const studyTime = ['08:40 - 09:20', '09:30 - 10:10',
    '10:20 - 11:00', '11:10 - 11:50', '11:50 - 12:40',
    '12:40 - 13:20', '13:30 - 14:10', '14:20 - 15:00'];

module.exports = {
    data: new SlashCommandBuilder().setName('수업시간').setDescription('수업시간을 표시합니다'),
    execute(interaction) {
        const embed = new MessageEmbed().setColor('#FFA7A7').setTitle('수업시간').setDescription('『조종례는 알잘딱』').setFooter({ text: 'paka#8285' });
        embed.addField('1교시', studyTime[0])
        embed.addField('2교시', studyTime[1])
        embed.addField('3교시', studyTime[2])
        embed.addField('4교시', studyTime[3])
        embed.addField('점심시간', studyTime[4])
        embed.addField('5교시', studyTime[5])
        embed.addField('6교시', studyTime[6])
        embed.addField('7교시', studyTime[7])
        interaction.reply({ embeds: [embed] });
    }
};
