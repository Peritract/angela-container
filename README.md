# Dev Container for Angela

This repo contains a small example of using Docker to run code inside a container but develop on your local machine.

## Requirements

- Docker needs to be running

## Development

Run `run-dev-container.sh`. This will start a container and connect to it using your terminal.

It will *also* mirror the `code` folder on your machine with a `code` folder on the container; any changes you make to either one will be mirrored inside the other.

This means that you can write code in your normal environment but have it accessible/runnable from within the container context (hopefully bypassing weird config issues).

## Important reminders

- Never run `pip install [anything]` from outside the container; only run it when your terminal is connected into the container, as otherwise you will end up with the wrong versions of libraries
- When you stop and restart the container, you'll need to remember to reinstall things

## Demo

To run the example code successfully, you'll need a `.env` file with the following data:

```sh
API_KEY=XXXXXXXXXX
API_URL=https://www.behindthename.com/api/lookup.json
NAME=XXXXX
```

Where `API_KEY` should be a key for the [Behind the Name API](https://www.behindthename.com/api/gateway.php) and name should be any name you choose.

