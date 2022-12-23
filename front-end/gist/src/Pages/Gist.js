import { Link } from "react-router-dom";
import Logo from "../Images/logo_2_rmbg.png";
import NavBar from '../Components/NavBar/NavBar'
import CardGrid from "../Components/Gist/Card_Grid";


function Gist(props){

return(
 
    <>
    <NavBar/>
    <div className="padding_header" id="Top"></div>
    <CardGrid/>
    </>

);

}

export default Gist;