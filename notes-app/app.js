const chalk = require("chalk");
const yargs = require("yargs");
const { hideBin } = require("yargs/helpers");
const notes = require("./notes.js");

yargs(hideBin(process.argv))
  .command(
    "add",
    "add a note",
    (yargs) => {
      return yargs
        .option("title", {
          alias: "t",
          type: "string",
          description: "Title of the note",
          demandOption: true,
        })
        .option("body", {
          alias: "b",
          type: "string",
          description: "The body of the note",
          demandOption: true,
        });
    },
    (argv) => {
      notes.addNote(argv.title, argv.body);
    }
  )
  .command(
    "remove",
    "remove a note",
    (yargs) => {
      return yargs.option("title", {
        alias: "t",
        type: "string",
        description: "Title of note to be deleted",
        demandOption: true,
      });
    },
    (argv) => {
      notes.removeNote(argv.title);
    }
  )
  .command(
    "read",
    "Read a note",
    (yargs) => {
      return yargs.option("title", {
        alias: "t",
        type: "string",
        description: "Get specific note",
        demandOption: true,
      });
    },
    (argv) => {
      notes.readNote(argv.title);
    }
  )
  .command(
    "list",
    "list all notes",
    (yargs) => {},
    (argv) => {
      notes.listNotes();
    }
  )
  .help()
  .parse();
