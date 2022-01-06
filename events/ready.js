module.exports = {
	name: 'ready',
	once: true,
	execute(client) {
		console.log(`Ready! Logged in as ${client.user.tag}`);
		client.user.setActivity("/시간표 | /수업시간", {
			type: "LISTENING"
		});
	},
};