import React from "react";
import ReactDOM from "react-dom";

import Home from "./components/pages/home";
import Contact from "./components/pages/contact";

if (window.location.pathname === "/") {
  ReactDOM.render(<Home />, document.getElementById("root"));
} else if (window.location.pathname === "/contact") {
  ReactDOM.render(<Contact />, document.getElementById("root"));
}
