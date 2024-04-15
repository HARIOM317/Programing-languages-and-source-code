import React from 'react'

const MyProfile = ({params}) => {
  return (
    <div>
      <h1>USER PROFILE - {params.id}</h1>
    </div>
  );
}

export default MyProfile
