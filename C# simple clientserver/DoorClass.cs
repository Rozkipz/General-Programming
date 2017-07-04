using System;

namespace doorclass
{
    [Serializable()]
    public class door
    {
        public int Id { get; set; }
        public string Label { get; set; }
        public bool Status { get; set; }
    }
}
//      csc /target:library /out:doorclass.DLL DoorClass.cs