export default function DashboardLayout({
  children,
  login,
  users,
  revenue,
  notifications,
}: {
  children: React.ReactNode;
  login: React.ReactNode;
  users: React.ReactNode;
  revenue: React.ReactNode;
  notifications: React.ReactNode;
}) {
  const isLoggedIn = false;

  return isLoggedIn ? (
    <div>
      <div>{children}</div>

      <div style={{ display: "flex", gap: "1rem" }}>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div>{users}</div>
          <div>{revenue}</div>
        </div>
        <div style={{ display: "flex", flex: 1 }}>{notifications}</div>
      </div>
    </div>
  ) : (
    <div>
      <div>{children}</div>

      <div style={{ display: "flex", flex: 1, minHeight: '75vh' }}>{login}</div>
    </div>
  );
}
