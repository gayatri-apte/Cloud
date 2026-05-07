package lab3;



import org.cloudbus.cloudsim.*;

import org.cloudbus.cloudsim.core.CloudSim;

import org.cloudbus.cloudsim.provisioners.BwProvisionerSimple;

import org.cloudbus.cloudsim.provisioners.PeProvisionerSimple;

import org.cloudbus.cloudsim.provisioners.RamProvisionerSimple;



import java.util.*;



public class SJFScheduler {

    public static void main(String[] args) throws Exception {



        CloudSim.init(1, Calendar.getInstance(), false);



        List<Host> h = new ArrayList<>();

        List<Pe> p = Arrays.asList(new Pe(0, new PeProvisionerSimple(1000)));



        h.add(new Host(0, new RamProvisionerSimple(2048),new BwProvisionerSimple(10000), 1000000,p, new VmSchedulerTimeShared(p)));



        Datacenter dc = new Datacenter("DC",

                new DatacenterCharacteristics("x86","Linux","Xen",h,10,3,0.05,0.001,0),

                new VmAllocationPolicySimple(h), new LinkedList<>(),0);



        DatacenterBroker b = new DatacenterBroker("B");



        b.submitVmList(Arrays.asList(

                new Vm(0,b.getId(),1000,1,512,1000,10000,"Xen",

                        new CloudletSchedulerTimeShared())

        ));



        List<Cloudlet> cl = new ArrayList<>();

        long[] l = {40000,20000,10000,30000};



        for(int i=0;i<l.length;i++){

            Cloudlet c = new Cloudlet(i,l[i],1,300,300,

                    new UtilizationModelFull(),

                    new UtilizationModelFull(),

                    new UtilizationModelFull());

            c.setUserId(b.getId());

            cl.add(c);

        }



        // 🔥 SJF (only core logic)

        cl.sort(Comparator.comparingLong(Cloudlet::getCloudletLength));



        b.submitCloudletList(cl);



        CloudSim.startSimulation();

        for(Cloudlet c: b.getCloudletReceivedList())

            System.out.println(c.getCloudletId()+" -> "+c.getCloudletLength());

        CloudSim.stopSimulation();

    }

}

