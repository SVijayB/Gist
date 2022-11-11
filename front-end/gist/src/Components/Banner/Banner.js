import { useNavigate} from 'react-router-dom'
import './Banner.css'

function Item(props){
  
    return(
        <div className="B_text"  onClick={props.clickHandler}>
            <div>{props.heading}</div>
            <div><p>{props.about}</p></div>
         </div>

    );

}
const about="Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."



function Banner(props){
    
    const navg=useNavigate();

    function RouteHandler(path){
        navg(path);
        console.log(path);
    }

    return(
        <>
          <div className="Banner_Section">
            <div className="Banner_Container">
                <Item heading="Summarizer" about={about} clickHandler={RouteHandler.bind(this,"/api")} />
                <Item heading="GIST" about={about} clickHandler={RouteHandler.bind(this,"/gist")} />
                <Item heading="Gmail Summarizer" about={about} clickHandler={RouteHandler.bind(this,"/gmail")}/>
            </div>
          </div>
        </>
    )


}

export default Banner;
