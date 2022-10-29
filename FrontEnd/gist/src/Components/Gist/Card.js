
import './card.css'


function Card(props){

return(

    <>
    <div className="card_container">
       <div className='card_header'>
        <img alt='img' src='https://wme-gep-drupal-hbo-prod.s3.amazonaws.com/2022-09/house-of-the-dragon-sn01-v2-ka-1920.jpg?w=640'/>
       </div>
       <div className='card_content'>
            <div className='card_meta_data'>
                 2 MONDAYS AT 10 PM
            </div>
            <div className='card_title'>
                TITLE 
            </div>
            <div className='card_data'>
              <p className='card_data_p'>
                Set 40 years in the future when traveling the solar system is big business,
                 this comedy series follows life on board Avenue 5, a mash-up of a cruise liner 
                 and an interplanetary rocket ship.
                 Set 40 years in the future when traveling the solar system is big business,
                 this comedy series follows life on board Avenue 5, a mash-up of a cruise liner 
                 and an interplanetary rocket ship.
              </p>
            </div>
       </div>
    </div>
    </>

);

}

export default Card;