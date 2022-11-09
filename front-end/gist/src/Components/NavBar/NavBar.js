import "./NavBar.css";
import { Link } from "react-router-dom";
import Logo from "../../Images/logo_2_rmbg.png";


function MyNavBar() {
  return (
    <header className="NavBar">
      <div className="NavBar_container">
        <div className="header_menu">
          <div>
            <Link to="/">
              <img src={Logo} alt="logo" className="Logo" />
            </Link>

            <h2>GIST</h2>
          </div>

          <div className="header_menu_list">
            <ul className="soln">
              <li>How It Works</li>
              <li>Pricing</li>
              <li className="product">
                Products
                 <ul className="product_list">
                  <li>Gmail Summarizer</li>
                  <li>API</li>
                  <li>GIST</li>
                 </ul>
              </li>
            </ul>
          </div>
        </div>

        <div className="user_actions">
          <button  type="button" className="user_btn">Log In</button>
          <button   type="button" className="user_btn active_btn" style={{color:"white",border: "2px solid #00B3B3"}}>Sign Up</button>
        </div>

        <div className="Mobile-icon">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </header>
  );
}

export default MyNavBar;
