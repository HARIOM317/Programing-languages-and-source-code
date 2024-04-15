"use client"
import { useRouter } from 'next/navigation'

const LearnUseRouter = () => {
    const router = useRouter();
  return (
    <div>
      <h1>Use Router</h1>

      <button type='button' onClick={() => router.push("/about")}>Go to about page</button>

      <button type='button' onClick={() => router.push("/blog/hsr")}>Show blogs</button>
    </div>
  )
}

export default LearnUseRouter
