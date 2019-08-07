import React from "react";
import Particles from "react-particles-js";
import particleConfig from "./../particleConfig";

function Banner() {
  return (
    <section id="slider_area" class="welcome-area">
      <Particles
        params={{ particles: particleConfig.particles }}
        style={{
          width: "100%",
          height: "100%",
          position: "absolute",
          top: 0
        }}
      />
      <div class="single-slide-item-table">
        <div class="single-slide-item-tablecell">
          <div class="container">
            <div class="row">
              <div class="col-md-7 col-sm-12 col-xs-12">
                <div class="single_slide_text">
                  <h1 class="slider_title animated">
                    Innovative & Educational Experience for the Perfect Pitch
                  </h1>
                  <p class="slider_subtitle animated">
                    Using VR on the Oculus Quest to tackle the lack of
                    repeatable, effective pitching practice for young
                    entrepreneurs
                  </p>
                  <a href="./contact" class="btn btn-default google_play">
                    Request a Demo
                  </a>
                </div>
              </div>
              <div class="col-md-5 text-center hidden-sm hidden-xs">
                <div class="slider_image animated">
                  <img
                    src="https://www.windowscentral.com/sites/wpcentral.com/files/field/image/2019/03/oculus-quest-cropped-01.png?itok=Pq-SfEZA"
                    alt=""
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Banner;
