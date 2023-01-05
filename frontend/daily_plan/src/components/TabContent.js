import React, { useState } from "react";
import { Segment, Icon } from "semantic-ui-react";
import { MDBInputGroup, MDBCheckbox, MDBRadio } from "mdb-react-ui-kit";
import InputItem from "./InputItem";

const TabContent = ({ showItems, edit }) => {
  const [input, setInput] = useState();
  const itemsList = showItems.map((item, i) => {
    return (
      <Segment key={i} color="violet" textAlign="center">
        <p style={{ height: "20px", padding: "50px,15px,0px,10px" }}>
          {" "}
          {item[0]}
        </p>
      </Segment>
    );
  });

  if (!edit) {
    return <>{itemsList}</>;
  } else {
    return <InputItem showItems={showItems} />;
  }
};
export default TabContent;
