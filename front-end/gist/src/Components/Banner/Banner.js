import { useNavigate} from 'react-router-dom'
import './Banner.css'

function Item(props){
  
    return(
         <div className='Banner_text ' id={props.bckId} onClick={props.clickHandler}>
            <div className='Banner_header'>{props.heading}</div>
         </div>

    );

}




function Banner(props){

    const aboutSummarizer =`For summarizing text, files, and news articles `
    const aboutGist = `Get one minute summary of news articles using gist `
    const aboutGmail = `Get a summary of your mails using Gmail Summarizer`
    
    const navg=useNavigate();

    function RouteHandler(path){
        navg(path);
        console.log(path);
    }

    return(
        <>
          <div className="Banner_Section" id="products&s">
            <div className='Team PandS'> Product and Service</div>
            <div className="Banner_Container">
                <Item heading="Summarizer" bckId='gistbackg'  about={aboutSummarizer} clickHandler={RouteHandler.bind(this,"/api")} />
                <Item heading="GIST"  bckId="newsbackg" about={aboutGist} clickHandler={RouteHandler.bind(this,"/gist")} />
                <Item heading="Gmail Summarizer" bckId="gmailsbackg" about={aboutGmail} clickHandler={RouteHandler.bind(this,"/gmail")}/>
            </div>
          </div>
        </>
    )


}

export default Banner;
