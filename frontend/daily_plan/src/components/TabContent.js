import React from "react";
import { Segment } from "semantic-ui-react";

const TabContent = ({ showItems }) => {
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
  return itemsList;
};
export default TabContent;
