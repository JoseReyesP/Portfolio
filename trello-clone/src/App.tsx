import React from "react";
import { AppContainer } from "./styles";
import { Column } from "./Column";
import { AddNewItem } from "./AddNewItem";

export function App() {
  return (
    <AppContainer>
      <Column text="TODO: "></Column>
      <AddNewItem toggleButtonText="+ Add another list" onAdd={console.log} />
    </AppContainer>
  );
}
