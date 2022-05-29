const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');
const moment = require('moment');
const { neisKey } = require('../config.json');
const request = require('request');

require('moment-timezone');
moment.tz.setDefault("Asia/Seoul");

const daylist = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'];

module.exports = {
	data: new SlashCommandBuilder()
		.setName('시간표')
		.setDescription('나이스에서 시간표 데이터를 찾아드립니다!')
		.addStringOption(option => option.setName("class").setDescription('원하는 반을 선택해주세요').addChoice('게임', '게임과1')
			.addChoice('네보1', '네트워크보안과1').addChoice('해킹1', '해킹보안과1').addChoice('해킹2', '해킹보안과2').setRequired(true))
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

		var str = argsClass.value;
		var regex = /[^0-9]/g;
		var result = str.replace(regex, '');
		var dddep = str.replace(result, '');

		var APTP_OFCDC_SC_CODE = 'B10';
		var SD_SCHUL_CODE = '7010911';
		var ALL_TI_YMD = String(moment().format('YYYYMMDD'));
		var DDDEP_NM = dddep;
		var GRADE = 2;
		var CLASS_NM = result;
		var reqUrl = `https://open.neis.go.kr/hub/hisTimetable?KEY=${neisKey}&Type=json&ATPT_OFCDC_SC_CODE=${APTP_OFCDC_SC_CODE}&SD_SCHUL_CODE=${SD_SCHUL_CODE}&ALL_TI_YMD=${ALL_TI_YMD}&DDDEP_NM=${encodeURI(DDDEP_NM)}&GRADE=${GRADE}&CLASS_NM=${CLASS_NM}`
		var reqOptions = { 'method': 'GET', 'url': reqUrl }

		request(reqOptions, function (error, response, body) {
			if (error) {
				console.error(err);
				interaction.reply({ content: '명령을 실행하는데 오류가 발생하였습니다...', ephemeral: true });
			} else {
				const jsonData = JSON.parse(body);
				if (!jsonData.hasOwnProperty('hisTimetable'))
				{
					if(jsonData.RESULT.CODE == "INFO-200"){
						const errorEmbed = new MessageEmbed().setColor('#FF0000').setTitle('오류').setDescription('나이스에서 데이터를 불러올 수 없습니다').setFooter({ text: 'paka#8285' });
						interaction.reply({ embeds: [errorEmbed] });
					}
				}
				else{
					if (jsonData.hisTimetable[0].head[1].RESULT.CODE != "INFO-000") {
						const errorEmbed = new MessageEmbed().setColor('#FF0000').setTitle('오류').setDescription('나이스에서 데이터를 불러올 수 없습니다').setFooter({ text: 'paka#8285' });
						interaction.reply({ embeds: [errorEmbed] });
					}
					else {
						if (!jsonData.hisTimetable[1].row) {
							const errorEmbed = new MessageEmbed().setColor('#FF0000').setTitle('오류').setDescription('시간표 데이터가 존재하지 않습니다').setFooter({ text: 'paka#8285' });
							interaction.reply({ embeds: [errorEmbed] });
						}
						else {
							await interaction.deferReply();

							function getRandomColor() {
								var letters = '0123456789ABCDEF';
								var color = '#';
								for (var i = 0; i < 6; i++) {
									color += letters[Math.floor(Math.random() * 16)];
								}
								return color;
							}
	
							const embed = new MessageEmbed().setColor(getRandomColor()).setTitle(`${DDDEP_NM} ${GRADE}-${CLASS_NM}`).setDescription(`${daylist[date]} ${DDDEP_NM} ${CLASS_NM}반 시간표 입니다!`).setFooter({ text: 'paka#8285' });
							jsonData.hisTimetable[1].row.forEach(element => {
								embed.addField(`${element.PERIO}교시`, `${element.ITRT_CNTNT}`, false);
							});
	
							interaction.reply({ embeds: [embed] });
						}
					}
				}
					
				
			}
		});
	},
};
