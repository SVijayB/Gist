import "./NavBar.css";
import { Link } from "react-router-dom";
import Logo from "../../Images/logo_2_rmbg.png";
import { Link as LinkS } from "react-scroll";
import Arrow from '../../Images/inky-arrow.png'

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
            <div className="soln">
                <LinkS to="products&s"
                smooth={true}
                duration={100}
                spy={true}
                exact="true"
                offset={-100}>
                PRODUCTS
                </LinkS>
                <LinkS to="AboutSection"    
                smooth={true}
                duration={100}
                spy={true}
                exact="true"
                offset={-100}>
                ABOUT
                </LinkS>
                <LinkS to="team"
                smooth={true}
                duration={100}
                spy={true}
                exact="true"
                offset={-100}>
                TEAM
                </LinkS>
            </div>
          </div>
        </div>

        <div className="user_actions">
          <LinkS  to="FooterH" className="user_btn"
            smooth={true}
            duration={100}
            spy={true}
            exact="true"
            offset={-100}>
              <img src={Arrow} alt="ArrowUp"/>  
          </LinkS>
          <LinkS  to="Top" className="user_btn" style={{background:"#fff"}}
            smooth={true}
            duration={100}
            spy={true}
            exact="true"
            offset={-100}>
             <img src={Arrow} alt="ArrowDown" id="DownArrow"/> 
          </LinkS>
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
