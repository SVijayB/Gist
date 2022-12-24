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
                       Gist is an online open-source tool that summarizes text, files, images and news articles
                        from several news sources using highly advanced artificial inteligence and NLP. 
                        Gist also summarizes mails for a quick overview of your gmail content in a glance.
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