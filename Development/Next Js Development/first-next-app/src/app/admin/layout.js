import AdminNavbar from "../../components/AdminNavbar";

export default function AdminLayout({children}) {
    return (
        <>
        <section>
            {/* Fixed admin navbar for all admin pages */}
            <AdminNavbar />
            {children}
        </section>
        </>
    );
}