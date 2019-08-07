import React from "react";

import Preloader from "./../preloader";
import Navbar from "./../navbar";
import Banner from "./../banner";
import HowItWorks from "./../howitworks";

function Home() {
  return (
    <div>
      <Preloader />
      <Navbar />
      <Banner />
      <HowItWorks />
    </div>
  );
}

export default Home;
