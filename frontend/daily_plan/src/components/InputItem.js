import React, { useCallback, useEffect, useRef, useState } from "react";
import { Grid, Icon } from "semantic-ui-react";
import "../App.css";

const InputItem = ({ showItems }) => {
  const [items, setItems] = useState([]);
  const [input, setInput] = useState("");
  const firstObj = useRef();

  useEffect(() => {
    const singleItems = showItems.map((list, i) => {
      return { id: i, task: list[0] };
    });
    setItems(singleItems);
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("sub", items);
  };
  const handleChange = (e) => {
    const id = parseInt(e.target.dataset.id, 10);
    let copy = [...items];
    const val = e.target.value;
    copy[id].task = val;
    setItems(copy);
  };
  const addItem = (e) => {
    setInput(e.target.value);
    let copy = [...items];
    copy = [...copy, { id: items.length + 1, task: input }];
    setItems(copy);
  };
  const deleteItem = (e) => {
    const index = parseInt(e.target.dataset.id, 10);
    let copy = [...items];
    copy.splice(index, 1);
    setItems(copy);
  };
  useEffect(() => {
    console.log(items);
  }, [items]);

  // const focus = () => {
  //   nameRef.current.focus();
  // };

  const itemInput = items.map((item, i) => {
    return (
      <Grid data-id={i} key={item.id}>
        <Grid.Column floated="left" width={15}>
          <input
            className="form-control pt-3"
            data-id={i}
            type="text"
            value={item.task}
            style={{ borderBottomColor: "BlueViolet" }}
            onChange={(e) => {
              handleChange(e);
            }}
            ref={i === 0 ? firstObj : null}
          />{" "}
        </Grid.Column>
        <Grid.Column>
          <Icon
            data-id={i}
            onClick={(e) => {
              deleteItem(e);
            }}
            className="trash "
            // disabled
            name="trash"
          />
        </Grid.Column>
      </Grid>
    );
  });
  if (items.length > 0) {
    return (
      <>
        <form>
          <div id="itemForm">{itemInput}</div> <br />
          <div>
            <div
              onClick={(e) => {
                addItem(e);
              }}
            >
              <Icon
                disabled
                name="add"
                size="large"
                color="black"
                className="hearts"
              />
            </div>
            <div>
              <input
                type="submit"
                style={{
                  float: "right",
                  marginRight: "10px",
                }}
                onClick={(e) => {
                  handleSubmit(e);
                }}
              />
            </div>
          </div>
        </form>
      </>
    );
  }
};
export default InputItem;
