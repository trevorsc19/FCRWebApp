import React from "react";

import Preloader from "./../preloader";
import Navbar from "./../navbar";
import ContactBanner from "../contact_banner";

function Contact() {
  return (
    <div>
      <Preloader />
      <Navbar />
      <ContactBanner />
    </div>
  );
}

export default Contact;
