import Link from "next/link";
import React from "react";

const LearnLink = () => {
  const id = 2;
  return (
    <>
      <Link href="/admin/dashboard">Go to admin dashboard</Link>
      <Link href={`/user/profile/${id}`}>Go to user profile</Link>
      <Link href="/user/settings">Go to user settings</Link>
    </>
  );
};

export default LearnLink;
