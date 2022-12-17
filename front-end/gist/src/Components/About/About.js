import AboutImg from '../../Images/about_img.svg'
import { useNavigate} from 'react-router-dom'
import './About.css';

function About(){
    
    const navg=useNavigate();

    function RouteHandler(path){
        navg(path);
    }

    return(
     
        <div className="About_container">
            <div className='abt_img rows'>
                <img src={AboutImg} alt="Reading"/>
            </div>
            <div className='abt_text rows'>
                 <div id="abt_h1">
                    <h2 id="abt_heading">GIST</h2>
                 </div>
                 <div id="abt_txt">
                    <h5>
                        Nulla pellentesque sapien risus, at dapibus sem condimentum sed. Quisque sed risus in felis porta rhoncus ac vel quam. 
                        Vivamus faucibus tincidunt libero ut blandit. Etiam ultricies mi vitae quam scelerisque rhoncus. Aenean eget purus facilisis, 
                        dictum lectus eu, luctus nunc. Praesent est risus, 
                        commodo a ex vel, imperdiet rhoncus ex. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
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