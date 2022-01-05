module.exports = {
    name: 'interactionCreate',
    execute(interaction, client) {
        console.log(`${interaction.user.tag} in #${interaction.channel.name} triggered an interaction.`);

        // command
        if (!interaction.isCommand()) return;

        const command = client.commands.get(interaction.commandName);

        if (!command) return;

        try {
            command.execute(interaction);
        } catch (error) {
            console.error(error);
            interaction.reply({ content: '명령을 실행하는데 오류가 발생하였습니다...', ephemeral: true });
        }
    },
};