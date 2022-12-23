
import { useEffect,useState } from "react";
import { GoogleLogin } from 'react-google-login';
import { gapi } from 'gapi-script';
import axios from "axios";
import Navbar from '../Components/NavBar/NavBar'
import Modal from "../Components/Modal/Modal";
import Footer from '../Components/Footer/Footer'
import { Link  as LinkS} from "react-scroll";

function Gmail(props){
  
  const [modal,setmodal] = useState(false);
  const [login,setlogin] = useState(false);
  const [Emails,SetEmails] = useState(5)
  const [btndisabled,setdisabled] = useState(false);
  

  useEffect(() => {
        function start() {
            gapi.client.init({
            clientId : "697219463966-o1vqvlgb5ctajehm0cip343mvlhs0n98.apps.googleusercontent.com",
            scope : 'openid email profile https://www.googleapis.com/auth/gmail.readonly'
        })};
    gapi.load('client:auth2',start);
    });
  const responseGoogle = (response) => {
    console.log(response)
    setdisabled(true);
    post_token(response);
  }
  const responseGoogleFailure = (response) => {
    console.log(response)
    setmodal(true);
    setlogin(false);
    
  }

  const OnDropdownHandlers = (event) =>{
      SetEmails(event.target.value)
  }

  const closeModal =()=>{
    setlogin(false);
    setmodal(false);
  }
  
  const post_token = (data) =>{
      axios.post(`http://127.0.0.1:5000/api/gmail/callback?NoEmails=${Emails}`,data).then((res)=>{
        console.log(res.data)
          setmodal(true);
          setlogin(true);
          setdisabled(false);
      }).catch(e=>{
        console.log(e);
        setmodal(true);
        setlogin(false);
        setdisabled(false);
      });
  }

return (
    <>
      <Navbar/>
     
     <div className="About_container">
        <Modal  open={modal} closebtn={closeModal} userlogin={login}/>
        {!modal?
        <div className="Gmail_container" id="Top">
          <div className="info_gmail_text">
            Login into your Gmail Account
          </div>
          <div className="GmailDropdown">
            <label htmlFor="No_of_mail">Number of Gmails to Summarize</label>
                <select name="No_of_mail" id="No_of_mail" defaultValue={5}onChange={OnDropdownHandlers}>
                  <option value="5">5</option>
                  <option value="10">10</option>
                  <option value="15">15</option>
                </select>
          </div>
            <GoogleLogin 
                      clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}
                      buttonText="Login"
                      onSuccess={responseGoogle}
                      onFailure={responseGoogleFailure}
                      cookiePolicy={'single_host_origin'}
                      responseType='code'
                      accessType='offline'
                      disabled={btndisabled}
              />
          <div className="info_gmail_text">
            Read Privacy Policy
          </div>
            <LinkS to='FooterH'> <div className="arrowIcon" ></div></LinkS>
          
        </div>:null
        }
       
      
     </div>
     {!modal?<Footer/>:null}
   
    </>

)

}


export default Gmail;

