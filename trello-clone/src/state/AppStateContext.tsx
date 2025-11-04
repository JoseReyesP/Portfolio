import { createContext, useContext, FC, ReactNode } from "react";

type Task = {
  id: string;
  text: string;
};

type List = {
  id: string;
  text: string;
  tasks: Task[];
};

export type AppState = {
  lists: List[];
};

const appData: AppState = {
  lists: [
    {
      id: "0",
      text: "To Do",
      tasks: [{ id: "c0", text: "Generate app Scaffold" }],
    },
    {
      id: "1",
      text: "In Progress",
      tasks: [{ id: "c2", text: "Learn typescript" }],
    },
    {
      id: "2",
      text: "Done",
      tasks: [{ id: "c3", text: "Begin to use static typing" }],
    },
  ],
};

type AppContextProps = {
  lists: List[];
  getTaskByListId(id: string): Task[];
};

const AppStateContext = createContext<AppContextProps>({} as AppContextProps);

type AppStateProviderProps = {
  children: ReactNode;
};

export const AppStateProvider: FC<AppStateProviderProps> = ({ children }) => {
  const { lists } = appData;

  const getTaskByListId = (id: string) => {
    return lists.find((list) => list.id === id)?.tasks || [];
  };

  return (
    <AppStateContext.Provider value={{ lists, getTaskByListId }}>
      {children}
    </AppStateContext.Provider>
  );
};
