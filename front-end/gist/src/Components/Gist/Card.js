
import './card.css'


function Card(props){
  let title=""
   if(typeof(props.t)!='object')
   title=props.t
  let dt=props.dt.split("T")
  let date=dt[0].split("").reverse().join("")
  let time=dt[1].substring(0,5)
  
return(

    <>
    <div className="card_container"  onClick={props.fn}  data-position={props.pos}>
       <div className='card_header' data-position={props.pos}>
        <img alt='img' loading="lazy" src={props.img} data-position={props.pos}/>
       </div>
       <div className='card_content' data-position={props.pos}>
            <div className='card_meta_data' data-position={props.pos}>
               <div data-position={props.pos}>{date.substring(0,6)+date.substring(6).split("").reverse().join("")}</div>
              <div data-position={props.pos}>{time}</div>
            </div>
            <div className='card_title' data-position={props.pos}>
              <b data-position={props.pos}>{title}</b> 
            </div>
            <div className='card_data' data-position={props.pos}>
              <p className='card_data_p' data-position={props.pos}>
                {props.summary}
              </p>
            </div>
       </div>
    </div>
    </>

);

}

export default Card;