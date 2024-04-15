import UserNavbar from "@/components/UserNavbar";

export default function UserLayout ({ children }) {
  return (
    <>
      {/* fixed user navbar for all user pages */}
      <UserNavbar />
      <section>{children}</section>
    </>
  );
};
