import React from "react";
import Particles from "react-particles-js";
import particleConfig from "./../particleConfig";

function ContactBanner() {
  const height = window.height + "px";
  return (
    <section id="slider_area" class="welcome-area" style={{ height: "100%" }}>
      <Particles
        params={{ particles: particleConfig.particles }}
        style={{
          width: "100%",
          position: "absolute",
          top: 0
        }}
      />
      <section class="section_padding">
        <div class="container">
          <div class="section_heading text-center">
            <h2 class="contact_header">Schedule a live demo</h2>
          </div>
          <div class="row">
            <div class="col-lg-4 col-md-offset-4">
              <div class="contact_form">
                <form
                  id="contact-form"
                  method="post"
                  action="contact.php"
                  enctype="multipart/form-data"
                >
                  <div class="row">
                    <div class="form-group col-md-12">
                      <input
                        type="text"
                        name="first_name"
                        class="form-control"
                        id="first-name"
                        placeholder="First Name"
                        required="required"
                      />
                    </div>
                    <div class="form-group col-md-12">
                      <input
                        type="text"
                        name="last_name"
                        class="form-control"
                        id="last-name"
                        placeholder="Last Name"
                        required="required"
                      />
                    </div>

                    <div class="form-group col-md-12">
                      <input
                        type="email"
                        name="email"
                        class="form-control"
                        id="email"
                        placeholder="Email"
                        required="required"
                      />
                    </div>

                    <div class="form-group col-md-12">
                      <input
                        type="phone"
                        name="phone"
                        class="form-control"
                        id="phone"
                        placeholder="Phone Number"
                        required="required"
                      />
                    </div>

                    <div class="form-group col-md-12">
                      <select name="role" class="form-control" id="role">
                        <option disabled selected>
                          Role
                        </option>
                        <option>Student</option>
                        <option>Investor</option>
                        <option>Professor</option>
                        <option>Other</option>
                      </select>
                    </div>

                    <div class="form-group col-md-12">
                      <textarea
                        rows="6"
                        name="inquiry"
                        class="form-control"
                        id="description"
                        placeholder="Inquiry details"
                        required="required"
                      />
                    </div>

                    <div class="col-md-4 center-block">
                      <input
                        type="submit"
                        value="Submit"
                        name="submit"
                        id="submit"
                        class="app_store"
                      />
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>
    </section>
  );
}

export default ContactBanner;
