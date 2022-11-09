import { Link } from "react-router-dom";
import Logo from "../Images/logo_2_rmbg.png";
import CardGrid from "../Components/Gist/Card_Grid";

function Gist(props){

return(
 
    <>
      <header className="NavBar">
      <div className="NavBar_container">
        <div className="header_menu">
           <div>
            <Link to="/">
              <img src={Logo} alt="logo" className="Logo" />
            </Link>
            <h2>GIST</h2>
          </div>
        </div>
      </div>
    </header>
    <div className="padding_header"></div>
    <CardGrid/>
    </>

);

}

export default Gist;