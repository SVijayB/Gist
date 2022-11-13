import './GistModal.css'
import Icon from '../../Images/power.svg'


function GistModal(props){
    if (!props.open) return null;
  let dt=props.dt.split("T")
  let date=dt[0].split("").reverse().join("")
  let time=dt[1].substring(0,5)
    return(
        <>
        <div className='gplaceholder'>
          <div className="GistoverlayContainer">
              <div className="GistmodalContainer">
                <img src={props.img==null?Icon:props.img} alt="New Pic" className="new_pic" />
                <div className="Gistcontentright">
                    <div className='Gistmodalcontent'>
                      <div className='date'><h4>{date.substring(0,6)+date.substring(6).split("").reverse().join("")}</h4></div>
                       <h2 className='title_news'>{props.title}</h2>
                       <div className='Time'>
                        <h4 >TIME : {time}</h4>
                        <div><a className='link' href={props.more} target="_blank"  rel="noreferrer"><h4>SOURCE : CLICK HERE</h4></a></div>
                       </div>
                       <div className='new_summary'>{props.summary}</div>
                      <div className='btnmodal'><button className='Gistmodalclose' onClick={props.closebtn} >CLOSE</button></div> 
                    </div>
                </div>
              </div>
          </div>
          </div>
        </>
    )


}

export default GistModal;