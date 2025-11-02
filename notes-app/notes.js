const fs = require("fs");
const chalk = require("chalk");

const getNotes = () => {
  return "Your notes ...";
};

const addNote = (title, body) => {
  const notes = loadNotes();

  const duplicateNote = notes.find((note) => note.title === title);

  if (!duplicateNote) {
    notes.push({
      title: title,
      body: body,
    });
    saveNotes(notes);
    console.log(chalk.green.inverse("New note added!"));
  } else {
    console.log(chalk.yellow.inverse("Note title taken!"));
  }
};

const removeNote = (title) => {
  const notes = loadNotes();
  const updatedNotes = notes.filter((note) => note.title !== title);
  if (notes.length > updatedNotes.length) {
    saveNotes(updatedNotes);
    console.log(chalk.green.inverse("Note has been deleted"));
  } else {
    console.log(chalk.red.inverse("No note found"));
  }
};

const listNotes = () => {
  const notes = loadNotes();
  notes.map((note) => console.log(chalk.white.inverse(note.title)));
};

const readNote = (title) => {
  const notes = loadNotes();
  const note = notes.find((note) => note.title === title);
  if (note) {
    console.log(chalk.white.inverse(note.title));
    console.log(note.body);
  } else {
    console.log(chalk.yellow.inverse("Note not found!"));
  }
};

const saveNotes = (notes) => {
  const dataJSON = JSON.stringify(notes);
  fs.writeFileSync("notes.json", dataJSON);
};

const loadNotes = () => {
  try {
    const dataBuffer = fs.readFileSync("notes.json");
    const dataJSON = JSON.parse(dataBuffer.toString());
    return dataJSON;
  } catch (error) {
    return [];
  }
};

module.exports = {
  getNotes: getNotes,
  addNote: addNote,
  removeNote: removeNote,
  listNotes: listNotes,
  readNote: readNote,
};
