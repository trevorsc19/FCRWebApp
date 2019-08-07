import React from "react";

function HowItWorks() {
  return (
    <section id="promo_area" class="section_padding">
      <div class="container">
        <div class="section_heading text-center">
          <h2>How it works</h2>
          <p>
            Using immersive VR experiences, entrepreneurs can practice their
            pitch in front of realistic investors and environments. <br />
            Our goal is to equip every entrepreneur with the speaking skills and
            practice to land investments crucial to the success of their
            company.
          </p>
        </div>
        <div class="row">
          <div class="col-md-4">
            <div class="single_promo">
              <div class="promo_icon">
                <i class="ti-microphone" />
              </div>

              <div class="promo_details">
                <h3>Pitch</h3>
                <p>
                  <b>Preparing for a pitch?</b> Grab an Oculus Quest and choose
                  one of our custom virtual reality scenes. Acclimate yourself
                  to what it feels like to pitch in front of real investors.
                </p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="single_promo">
              <div class="promo_icon">
                <i class="ti-stats-up" />
              </div>

              <div class="promo_details">
                <h3>Feedback</h3>
                <p>
                  <b>Feedback is a gift.</b> Check out your metrics page to see
                  what areas you did well on and where you could improve.
                  Incorporate the personalized suggestions to your next
                  practice.
                </p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="single_promo">
              <div class="promo_icon">
                <i class="ti-infinite" />
              </div>

              <div class="promo_details">
                <h3>Repeat</h3>
                <p>
                  <b>Practice makes perfect!</b> Keep practicing your pitch
                  until you’re happy with your metrics and feedback and feel
                  confident enough to raise funding for your own company!
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default HowItWorks;
