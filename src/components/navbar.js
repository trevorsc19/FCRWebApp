import React from "react";

function Navbar() {
  return (
    <div class="navbar navbar-default navbar-fixed-top menu-top">
      <div class="container">
        <div class="navbar-header">
          <button
            type="button"
            class="navbar-toggle"
            data-toggle="collapse"
            data-target=".navbar-collapse"
          >
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar" />
            <span class="icon-bar" />
            <span class="icon-bar" />
          </button>
          <a href="./" class="navbar-brand">
            <span class="logo-text">vrware</span>
          </a>
        </div>

        <div class="navbar-collapse collapse">
          <nav>
            <div class="nav navbar-nav navbar-right">
              <ul class="nav navbar-nav">
                <li>
                  <a href="#promo_area">How it works</a>
                </li>
                <li>
                  <a href="./contact">Request a Demo</a>
                </li>
                <li>
                  <a href="./audioRecording">Practice</a>
                </li>
                <li>
                  <a href="./login">Login</a>
                </li>
              </ul>
            </div>
          </nav>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
