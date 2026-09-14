import GXB from "@/src/components/ui/GXB";

export default function Home() {
  return (
    <main id="main-content" tabIndex={-1} className="flex flex-1">
      <h1 className="sr-only">Home</h1>
      <GXB text="Welcome — the starting point of your new NextJS project." />
    </main>
  );
}
