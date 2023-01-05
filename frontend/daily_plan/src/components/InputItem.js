import React from "react";
import { Segment, Icon } from "semantic-ui-react";
import {
  MDBContainer,
  MDBNavbar,
  MDBNavbarBrand,
  MDBBtn,
  MDBInput,
} from "mdb-react-ui-kit";

const InputItem = ({ showItems }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("mama");
  };
  const itemInput = showItems.map((item, i) => {
    return (
      <div className="pt-3">
        {/* <MDBInputGroup
          className="mb-3"
          textTag="div"
          textAfter={<MDBCheckbox style={{ backgroundColor: "black" }} />}
        > */}
        <input
          className="form-control pt-3"
          type="text"
          value={item}
          style={{ borderBottomColor: "BlueViolet" }}
          onChange={() => {}}
        />
        {/* <MDBCheckbox style={{ backgroundColor: "black" }} /> */}
        {/* </MDBInputGroup> */}
      </div>
    );
  });
  return (
    <>
      <form>
        {itemInput} <br />
        <div>
          <Icon disabled name="add" size="large" color="black" />
          <input
            type="submit"
            style={{
              float: "right",
              marginRight: "10px",
            }}
          />
        </div>
      </form>
    </>
  );
};
export default InputItem;
