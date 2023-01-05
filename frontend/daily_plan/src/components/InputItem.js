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
  const addInput = (e) => {
    e.preventDefault();
    const tag = document.createElement("INPUT");
    tag.setAttribute("type", "text");
    tag.className = "form-control pt-3 mt-3";
    tag.style.borderBottomColor = "BlueViolet";
    tag.style.MarginTop = "30px";

    var element = document.getElementById("itemForm");
    tag.addEventListener("input", (e) => {
      handleSubmit(e);
    });
    element.appendChild(tag);
  };
  const handleSubmit = (e) => {
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
          key={i}
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
        <div id="itemForm">{itemInput}</div> <br />
        <div>
          <div
            onClick={(e) => {
              addInput(e);
            }}
          >
            <Icon disabled name="add" size="large" color="black" />
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
};
export default InputItem;
