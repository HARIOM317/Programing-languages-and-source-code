import Card from "@/components/card";
import React from "react";
import Link from "next/link";

const ArchivedNotifications = () => {
  return (
    <Card>
      <div>Archived Notifications</div>
      <div>
        <Link
          href={"/complex-dashboard"}
          style={{ color: "skyblue", fontWeight: "500" }}
        >
          Default
        </Link>
      </div>
    </Card>
  );
};

export default ArchivedNotifications;
