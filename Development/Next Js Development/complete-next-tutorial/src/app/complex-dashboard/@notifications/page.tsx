import Card from "@/components/card";
import React from "react";
import Link from "next/link";

const Notifications = () => {
  return (
    <Card>
      <div>Notifications</div>
      <Link
        href={"/complex-dashboard/archived"}
        style={{ color: "skyblue", fontWeight: "500" }}
      >
        Archived
      </Link>
    </Card>
  );
};

export default Notifications;
