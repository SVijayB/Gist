import './GistModal.css'
import Icon from '../../Images/power.svg'


function GistModal(props){
    if (!props.open) return null;
  let dt=props.dt.split("T")
  let date=dt[0].slice(-2)+'-'+dt[0].slice(-5,-3)+'-'+dt[0].slice(-10,-6)
  let time=dt[1].substring(0,5)
    return(
        <>
        <div className='gplaceholder'>
          <div className="GistoverlayContainer">
              <div className="GistmodalContainer">
                <div className='flex_img'><img src={props.img==null?Icon:props.img} alt="New Pic" className="new_pic" /></div>
                <div className="Gistcontentright">
                    <div className='Gistmodalcontent'>
                      <div className='date'><h4>{date.substring(0,6)+date.substring(6).split("").reverse().join("")}</h4></div>
                       <h2 className='title_news'>{props.title}</h2>
                       <div className='Time'>
                        <h6 >TIME : {time}</h6>
                        <div><a className='link' href={props.more} target="_blank"  rel="noreferrer"><h6>SOURCE : CLICK HERE</h6></a></div>
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