# Network and Cards Part 1
This week we are creating a game playable over network. This will be a 3-parter.

The first part is to set up a connection between a server and one or more client. The server needs to send out a heartbeat message to the clients and the clients need to respond to it.

For those who want to be prepared, we are going to deal and play cards over the network.
Formal Inputs & Outputs

## Input description

No input for the server, but the client needs to know where the server is.

## Output description

The client needs to echo the heartbeat from the server.

## Notes/Hints

The server needs to able to handle multiple clients in the end, so a multithreaded approach is advised. It is advised to think of some command like pattern, so you can send messages to the server and back.

For the server and client, just pick some random ports that you can use. Here you have a list off all "reserved" ports.

For the connection, TCP connections are the easiest way to do this in most languages. But you are not limited to that if you want to use something more high-level if your language of choice supports that.
Bonus

-    Make the server broadcast it's existince on the network, so clients can detect him.
-   Send messages to the server and broadcast it to all the clients
-    Let the client identify itself (username)
-    Create a way to list all connected clients
-   Send messages to the server and relay it to a requested client

These bonuses are not required, but it will make the next part a whole lot easier.'

# Network and Cards Part 2

The second part is less dry then the first part. We are going to play a simplyfied version of blackjack over the network. The server will deal cards over the network to all connected clients, there is no dealer stack like in real blackjack.

When all connected clients send a START command, the game will begin, you don't have to look for other connections then.

The communication goes as followed:

- SERVER -> CLIENT A: TAKE or PASS
- CLIENT A -> SERVER: TAKE
- SERVER -> CLIENT A: HEARTS QUEEN

- SERVER -> CLIENT B: TAKE or PASS
- CLIENT B -> SERVER: PASS

The client has the option to either respond with a TAKE command or PASS command, the server then go to the next client till everyone is done (all passed or everyone has 21 or more in score)

The cards have the following values:

2 -> 2
3 -> 3
4 -> 4
5 -> 5
6 -> 6
7 -> 7
8 -> 8
9 -> 9
Jack -> 10
Queen -> 10
King -> 10
Ace -> 1 or 11 (11 if not over 21 and 1 if over)

## Input description

 ### Server

Server has to accept at least 3 commands: START, TAKE and PASS

 ### Client

    Clients must be able to recieve the choice for TAKE and PASS and must be able to recieve cards, format of that is up to you

## Output description

 ### Server

    No Output required, but I can imagen that some loggin will be handy.
        Client

    A decent output for humans to read the cards and see their current score. Also must know when to type in the option to TAKE and PASS

## Notes/Hints
### TCP Socket approach

The server needs to able to handle multiple clients in the end, so a multithreaded approach is advised. It is advised to think of some command like pattern, so you can send messages to the server and back.

For the server and client, just pick some random ports that you can use. Here you have a list off all "reserved" ports.

For the connection, TCP connections are the easiest way to do this in most languages. But you are not limited to that if you want to use something more high-level if your language of choice supports that.
REST api approach

Some off you pointed out that this could be done with a webserver. If this is more in the line of what you are used to, no problem then, as long as it stays in the line of a multiplayer game.
Bonus

    Send all the events to other clients in the form CLIENT A takes a Queen of Hearts or Client A passes
    Allow clients to join when a game is running for the next game
    Add a spectator mode, nothing more fun then Let's play no?

# Network and Cards part 3

This week we are creating a game playable over network. This will be a 3-parter.

The third part is going to be even more interaction, and some cheating, card players love to cheat.

We are going to play a modified version of Blackjack:

Each player is dealt 1 covered card at the start of the game. When a player decides to take a card het recieves that card covered and then has to decide which one to play and which one to hold. Player send the card open over the network back to the server.

Starting stays the same: When all connected clients send a START command, the game will begin, you don't have to look for other connections then.

The communication goes as followed:

CLIENT A -> SERVER: START
CLIENT B -> SERVER: START

SERVER -> CLIENT A: Ace of spades
SERVER -> CLIENT B: 4 of clubs

SERVER -> CLIENT A: TAKE or PASS
CLIENT A -> SERVER: TAKE
SERVER -> CLIENT A: Queen of hearts
CLIENT A -> SERVER: PLAY Ace of spades

SERVER -> CLIENT B: TAKE or PASS
CLIENT B -> SERVER: PASS

The client has the option to either respond with a TAKE command, folowed by a PLAY or PASS command, the server then go to the next client till everyone is done (all passed or everyone has 21 or more in score)

The cards have the following values:

2 -> 2
3 -> 3
4 -> 4
5 -> 5
6 -> 6
7 -> 7
8 -> 8
9 -> 9
Jack -> 10
Queen -> 10
King -> 10
Ace -> 1 or 11 (11 if not over 21 and 1 if over)

## Input description

  ###  Server

Server has to accept at least 4 commands: START, TAKE, PLAY and PASS

   ### Client

    Clients must be able to recieve the choice for TAKE and PASS and must be able to recieve cards, format of that is up to you

## Output description

   ### Server

    No Output required, but I can imagen that some loggin will be handy.
        Client

    A decent output for humans to read the cards and see their current score. Also must know when to type in the option to TAKE and PASS

# Notes/Hints
## TCP Socket approach

The server needs to able to handle multiple clients in the end, so a multithreaded approach is advised. It is advised to think of some command like pattern, so you can send messages to the server and back.

For the server and client, just pick some random ports that you can use. Here you have a list off all "reserved" ports.

For the connection, TCP connections are the easiest way to do this in most languages. But you are not limited to that if you want to use something more high-level if your language of choice supports that.
REST api approach

Some off you pointed out that this could be done with a webserver. If this is more in the line of what you are used to, no problem then, as long as it stays in the line of a multiplayer game.

