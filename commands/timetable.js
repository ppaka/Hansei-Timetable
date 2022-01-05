const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');
const wait = require('util').promisify(setTimeout);
const fs = require('fs');
const moment = require('moment');

require('moment-timezone');
moment.tz.setDefault("Asia/Seoul");

const subjectInfos = {
	'컴그': ['컴그', '351 971 4354'], '국어': ['국어', '531 696 3430'], '영어': ['영어', '974 976 2480'], '사회': ['사회', '458 265 2826'], '국사': ['국사', '418 692 2475'], '수학': ['수학', '531 978 5696'],
	'프로': ['프로', '274 223 4806'], '과학': ['과학', '314 911 3899'], '진로': ['진로', '341 183 8871'], '음악': ['음악', '373 769 7752'], '디자': ['디자', '351 971 4354'], '체육': ['체육', '517 857 7141'],
	'자율': ['', ''], '정처': ['', ''], '파이썬': ['파이썬', '997 912 0043'], '파이썬1': ['파이썬', '948 102 7800'], '컴시': ['컴시', '279 718 8506'], '소양0': ['소양', '코드 몰라 ㅅㅂ'], '소양1': ['소양', '코드 몰라 ㅅㅂ'], '소양2': ['소양', '458 265 2826'], '소양3': ['소양', '418 692 2475']
};
const daylist = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'];

const zoomLink = 'https://zoom.us/j/';

module.exports = {
	data: new SlashCommandBuilder()
		.setName('시간표')
		.setDescription('시간표!')
		.addStringOption(option => option.setName("class").setDescription('원하는 반을 선택해주세요').addChoice('게임', '게임')
			.addChoice('해킹1', '해킹1').addChoice('해킹2', '해킹2').addChoice('해킹3', '해킹3').setRequired(true))
		.addIntegerOption(optiontwo => optiontwo.setName("day").setDescription('원하는 요일의 시간표를 볼때 사용합니다').addChoice('월요일', 1)
			.addChoice('화요일', 2).addChoice('수요일', 3).addChoice('목요일', 4).addChoice('금요일', 5).setRequired(false)),
	execute(interaction) {
		const argsClass = interaction.options["_hoistedOptions"].filter((object) => {
			return object['name'] === 'class'
		})[0];
		const argsDay = interaction.options["_hoistedOptions"].filter((object) => {
			return object['name'] === 'day'
		})[0];
		var date = moment().weekday();
		if (argsDay != null) {
			date = argsDay.value;
		}

		const jsonFile = fs.readFileSync('./timetables.json', 'utf8');

		if (argsClass.value == '게임') {
			const classData = JSON.parse(jsonFile).classGame;

			if (classData == null) {
				const errorEmbed = new MessageEmbed().setColor('#FF0000').setTitle('오류').setDescription('시간표 데이터가 존재하지 않습니다').setFooter({ text: 'paka#8285' });
				interaction.reply({ embeds: [errorEmbed] });
			}
			else {
				const embed = new MessageEmbed().setColor('#FFB2D9').setTitle('게임과 1-1').setDescription(`${daylist[date]} 게임 1반 시간표 입니다!`).setFooter({ text: 'paka#8285' });
				classData[date].subjects.forEach(subject => {
					embed.addField(subjectInfos[subject][0], `${subjectInfos[subject][1]}\n${zoomLink + subjectInfos[subject][1].replaceAll(' ', '')}`, false);
				});

				interaction.reply({ embeds: [embed] });
			}
		}
		else if (argsClass.value == '해킹1') {
			const classData = JSON.parse(jsonFile).classHac1;
			if (classData == null) {
				const errorEmbed = new MessageEmbed().setColor('#FF0000').setTitle('오류').setDescription('시간표 데이터가 존재하지 않습니다');
				interaction.reply({ embeds: [errorEmbed] });
			}
			else {
				const embed = new MessageEmbed().setColor('#B5B2FF').setTitle('해킹보안 1-1').setDescription(`${daylist[date]} 해킹보안 1반 시간표 입니다!`).setFooter({ text: 'paka#8285' });
				classData[date].subjects.forEach(subject => {
					embed.addField(subjectInfos[subject][0], `${subjectInfos[subject][1]}\n${zoomLink + subjectInfos[subject][1].replaceAll(' ', '')}`, false);
				});

				interaction.reply({ embeds: [embed] });
			}
		}
		else if (argsClass.value == '해킹2') {
			const classData = JSON.parse(jsonFile).classHac2;
			if (classData == null) {
				const errorEmbed = new MessageEmbed().setColor('#FF0000').setTitle('오류').setDescription('시간표 데이터가 존재하지 않습니다');
				interaction.reply({ embeds: [errorEmbed] });
			}
			else {
				const embed = new MessageEmbed().setColor('#CEF279').setTitle('해킹보안 1-2').setDescription(`${daylist[date]} 해킹보안 2반 시간표 입니다!`).setFooter({ text: 'paka#8285' });

				classData[date].subjects.forEach(subject => {
					embed.addField(subjectInfos[subject][0], `${subjectInfos[subject][1]}\n${zoomLink + subjectInfos[subject][1].replaceAll(' ', '')}`, false);
				});

				interaction.reply({ embeds: [embed] });
			}
		}
		else if (argsClass.value == '해킹3') {
			const classData = JSON.parse(jsonFile).classHac3;
			if (classData == null) {
				const errorEmbed = new MessageEmbed().setColor('#FF0000').setTitle('오류').setDescription('시간표 데이터가 존재하지 않습니다');
				interaction.reply({ embeds: [errorEmbed] });
			}
			else {
				const embed = new MessageEmbed().setColor('#FFC19E').setTitle('해킹보안 1-3').setDescription(`${daylist[date]} 해킹보안 3반 시간표 입니다!`).setFooter({ text: 'paka#8285' });

				classData[date].subjects.forEach(subject => {
					embed.addField(subjectInfos[subject][0], `${subjectInfos[subject][1]}\n${zoomLink + subjectInfos[subject][1].replaceAll(' ', '')}`, false);
				});

				interaction.reply({ embeds: [embed] });
			}
		}
	},
};