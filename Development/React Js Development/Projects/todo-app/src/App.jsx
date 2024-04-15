import React, { useState } from "react";
import "./index.css";
import ToDoList from "./ToDoList";

const App = () => {
  const [inputList, setInputList] = useState("");
  const [items, setItems] = useState([]); // hooks of array

  const itemEvent = (event) => {
    setInputList(event.target.value);
  };

  const listOfItems = () => {
    setItems((items) => {
      return [...items, inputList];
    });
    setInputList("");
  };

  const deleteItem = (id) => {
    setItems((oldItems) => {
      return oldItems.filter((arrElement, index) => {
        return index !== id;
      });
    });
  };

  return (
    <>
      <div className="main-div">
        <div className="center-div">
          <br />
          <h1>ToDo List</h1>
          <br />
          <input
            type="text"
            placeholder="Add an Item"
            onChange={itemEvent}
            value={inputList}
          />
          <button onClick={listOfItems}> + </button>

          <ol>
            {items.map((value, index) => {
              return (
                <ToDoList
                  key={index}
                  id={index}
                  text={value}
                  onSelect={deleteItem}
                />
              );
            })}
          </ol>
        </div>
      </div>
    </>
  );
};

export default App;
