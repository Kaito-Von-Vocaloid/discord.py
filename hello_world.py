import os
import discord
import random

client = discord.Client()

prefix = 'g!';

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

list = {
	"javascript": "console.log('Hello World!');",
	"html": "<h1>Hello World!</h1>",
	"c#": 'namespace HelloWorld\n{\n  class Hello {\n    static void Main(string[] args)\n    {\n      System.Console.WriteLine("Hello World!");\n    }\n  }\n}',
	"c": '#include <stdio.h>\nint main(){\n  printf("Hello World!")\n  return 0\n}',
	"c++": '#include <streamio>\nint main(){\n  std::cout << "Hello World!"\n  return 0\n}',
	"ruby": "puts 'Hello World!'",
	"python": 'print("Hello World!")',
	"php": 'echo "Hello World!"',
	"go": 'package main\nimport "fmt"\nfunc main(){\n  fmt.Println("Hello World!")\n}',
	"kotlin": 'fun main(args: Array<string>){\n  println("Hello World!")\n}',
	"java": 'class HelloWorld{\n  public static void main(String[] args){\n    System.out.println("Hello World!");\n  }\n}'
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	commandName = prefix+'hello-world'
	if message.content.startswith(commandName):
		arg = message.content[len(commandName):].replace(' ', '')
		if(arg == 'list'):
			myEmbed = discord.Embed(title="List of languaged you can see:", color=random.choice(colors))
			for e in list.keys():
				myEmbed.add_field(name=e, value="A programing language you can use for this command.")
			await message.reply(embed=myEmbed)
		elif(arg in list):
			await message.reply("```" + arg + "\n" + list[arg] + "\n```")
		else:
			await message.reply("Cannot found command, use `" + commandName + " list` to see available commands.")
        

client.run(os.getenv('TOKEN'))
