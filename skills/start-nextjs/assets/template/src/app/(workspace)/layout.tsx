import Footer from "@/src/components/ui/Footer";
import Header from "@/src/components/ui/Header";

export default function WorkspaceLayout({ children }: LayoutProps<"/">) {
  return (
    <>
      <Header />
      {children}
      <Footer />
    </>
  );
}
