const fs = require('fs');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const { clientId, guildId, token } = require('./config.json');

const commands = [];
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
        const command = require(`./commands/${file}`);
        commands.push(command.data.toJSON());
}

const rest = new REST({ version: '9' }).setToken(token);

// const guild = client.guilds.cache.get("<guild id>");

// This takes ~1 hour to update
client.application.commands.set([]);
// This updates immediately
// guild.commands.set([]);
