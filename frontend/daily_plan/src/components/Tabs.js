import React, { useEffect, useState } from "react";
import {
  MDBTabs,
  MDBTabsItem,
  MDBTabsLink,
  MDBTabsContent,
  MDBTabsPane,
  MDBRow,
  MDBCol,
} from "mdb-react-ui-kit";
import TabContent from "./TabContent";

const names = {
  Susan: [
    ["Visit Latra offices for Latra of T162 CML"],
    ["Request for petty cash"],
    ["Supervise Tabora rental"],
  ],
  Moses: [
    ["Follow up on Tanga parts to be sent to Mwanza"],
    ["Ensure Mwanza fines are paid"],
    ["Follow up on Biharamulo yard contract"],
    ["Follow up on RTS security payment"],
  ],
  Richard: [["Latra negotiation"], ["Seek grader invoice"]],
  Happiness: [
    ["Visiting Colgate Palmolive"],
    ["Assisting on for tyres quotation to Ecolab"],
    ["Preparing letters for disposal logbook release"],
    ["Handling T172 CWL rental "],
  ],
};

export default function Tabs({ edit, removeEdit }) {
  const [verticalActive, setVerticalActive] = useState("SUSAN");
  const [itemToShow, setItemToShow] = useState("SUSAN");
  const [showItems, setShowItems] = useState([]);
  const [rmEdit, unsetEdit] = useState(edit);
  const handleVerticalClick = (value) => {
    removeEdit(false);
    if (value === verticalActive) {
      return;
    }
    setVerticalActive(value);
  };
  useEffect(() => {
    for (const [key, value] of Object.entries(names)) {
      if (key === verticalActive) {
        setShowItems(value);
        setItemToShow(key);
        unsetEdit(true);
      }
    }
  }, [verticalActive]);

  const namesList = Object.keys(names);
  const nameTab = namesList.map((name, i) => {
    return (
      <MDBTabsItem key={i}>
        <MDBTabsLink
          style={{
            backgroundColor: "aliceblue",
            fontSize: "13px",
            fontFamily: "cursive",
          }}
          onClick={() => handleVerticalClick(name)}
          active={verticalActive === name}
        >
          {name}
        </MDBTabsLink>
      </MDBTabsItem>
    );
  });

  return (
    <>
      <MDBRow style={{ backgroundColor: "white" }}>
        <MDBCol size="3">
          <MDBTabs
            style={{ backgroundColor: "blue" }}
            className="flex-column text-center"
          >
            {nameTab}
          </MDBTabs>
        </MDBCol>
        <MDBCol size="9">
          <MDBTabsContent>
            <MDBTabsPane
              // style={{ backgroundColor: "purple" }}
              show={verticalActive === itemToShow}
              className="pt-3"
            >
              <TabContent showItems={showItems} edit={edit} />
            </MDBTabsPane>
          </MDBTabsContent>
        </MDBCol>
      </MDBRow>
    </>
  );
}
