const Discord = require('discord.js');

const client = new Discord.Client();



client.on('ready', () => {

    console.log('I am ready!');

});



client.on('message', message => {

    if (message.content === 'ping') {

        message.reply('pong');

    }

});


client.login(process.env.Iilwyof8 - Vc9wk8mKk4lU4rAhwVFjU9y);