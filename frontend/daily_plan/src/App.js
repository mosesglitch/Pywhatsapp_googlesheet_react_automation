import React, { useState } from "react";
import { MDBContainer, MDBNavbar, MDBNavbarBrand } from "mdb-react-ui-kit";
import "./App.css";
import "mdb-react-ui-kit/dist/css/mdb.min.css";
import { Icon, Button } from "semantic-ui-react";
import Tabs from "./components/Tabs";
import { RxPencil2 } from "react-icons/ti";

function App() {
  const [edit, setEdit] = useState(false);
  const editItems = () => {
    console.log("hallo");
    setEdit(true);
  };
  const removeEdit = (value) => {
    setEdit(value);
  };
  return (
    <>
      <div className="pt-5 mt-3">
        <MDBContainer>
          <MDBNavbar
            expand="lg"
            color="light"
            bgColor="dark"
            style={{ height: "50px" }}
          >
            <MDBContainer fluid>
              {" "}
              <MDBNavbarBrand
                href="#"
                style={{
                  color: "white",
                  fontFamily: "cursive",
                  fontSize: "25px",
                  padding: "10px",
                }}
              >
                Daily plan
              </MDBNavbarBrand>
              {!edit && (
                <Icon
                  className="hearts"
                  name="edit outline"
                  size="large"
                  onClick={() => {
                    editItems();
                  }}
                />
              )}
            </MDBContainer>
          </MDBNavbar>
          <Tabs edit={edit} removeEdit={removeEdit} />
        </MDBContainer>
      </div>
    </>
  );
}

export default App;
