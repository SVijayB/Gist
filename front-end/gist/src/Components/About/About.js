import AboutImg from '../../Images/about_img.svg'
import { useNavigate} from 'react-router-dom'
import './About.css';

function About(){
    
    const navg=useNavigate();

    function RouteHandler(path){
        navg(path);
    }

    return(
     
        <div className="About_container" id="Top">
            <div className='abt_img rows'>
                <img src={AboutImg} alt="Reading"/>
            </div>
            <div className='abt_text rows'>
                 <div id="abt_h1">
                    <h2 id="abt_heading">GIST</h2>
                 </div>
                 <div id="abt_txt">
                    <h5>
                        The gist is an online open-source tool for summarizing text, files, and news articles using our  Summarizer 
                        Get one minute summary of news articles using gist and Get a summary of your mails using Gmail Summarizer
                    </h5>
                 </div>
                 <div id="abt_btn">
                    <button  type="button" className="abtuser_btn" onClick={RouteHandler.bind(this,"/gist")}> News </button>
                    <button   type="button" className="abtuser_btn" onClick={RouteHandler.bind(this,"/api")}
                    style={{marginLeft:"15px"}} >Summarizer</button>
                 </div>
            </div>
        
        </div>

    );



}


export default About;